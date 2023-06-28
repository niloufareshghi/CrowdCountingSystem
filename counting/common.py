from datetime import datetime
from CrowdCountingModels.MSFANet.model import msfanet
from CrowdCountingModels.CAN.model import can_prediction
from CrowdCountingModels.MSFANet.model import msfa_prediction
from CrowdCountingModels.P2P.model import p2p_prediction
from CrowdCountingModels.VGG16 import extract_features

from counting.models import Submission


def count_and_store(submission_id, method):
    submission = Submission.objects.get(id=submission_id)
    submission.status = Submission.RUNNING
    submission.save()
    features = extract_features(submission.file)
    count = -1
    pred = ""
    try:
        if method == "msfa":
            count = msfanet(submission.file)
            pred = str(msfa_prediction(features))
            submission.model_name_desc = "MSFANet: Encoder-Decoder Based Convolutional Neural Networks with" \
                                         " Multi-Scale-Aware Modules for Crowd Counting"
        elif method == "can":
            submission.model_name_desc = "CAN: an end-to-end trainable deep architecture that combines features " \
                                         "obtained " \
                                         "using multiple receptive field sizes and learns the importance of each such " \
                                         "feature at each image location. In other words, our approach adaptively " \
                                         "encodes the scale of the contextual information required to accurately " \
                                         "predict crowd density. This yields an algorithm that outperforms " \
                                         "state-of-the-art crowd counting methods, especially when perspective " \
                                         "effects are strong. "
            pred = str(can_prediction(features))

        elif method == "p2p":
            submission.model_name_desc = "P2P: A Point-to-Point Network (P2PNet) is proposed to directly predict the " \
                                         "position of the center point of the head in the crowd. It is an intuitive " \
                                         "and concise example model based on the framework mentioned above. The " \
                                         "network has simple, " \
                                         "intuitive and high-precision features, and can serve as a new benchmark in " \
                                         "the industry. "
            pred = str(p2p_prediction(features))
        elif method == "smart":
            a = can_prediction(features)
            b = p2p_prediction(features)
            c = msfa_prediction(features)
            if b == 0:
                submission.model_name_desc = "P2P: A Point-to-Point Network (P2PNet) is proposed to directly predict " \
                                             "the position of the center point of the head in the crowd. It is an " \
                                             "intuitive and concise example model based on the framework mentioned " \
                                             "above. The network has simple, intuitive and high-precision features, " \
                                             "and can serve as a new benchmark in the industry. "
            elif b == 1 and (a == 0 and c == 0):
                submission.model_name_desc = "MSFANet: Encoder-Decoder Based Convolutional Neural Networks with" \
                                             " Multi-Scale-Aware Modules for Crowd Counting"
            elif b == 1 and (a == 0 and c == 1):
                submission.model_name_desc = "CAN: an end-to-end trainable deep architecture that combines features " \
                                             "obtained using multiple receptive field sizes and learns the importance " \
                                             "of each such " \
                                             "feature at each image location. In other words, our approach adaptively " \
                                             "encodes the scale of the contextual information required to accurately " \
                                             "predict crowd density. This yields an algorithm that outperforms " \
                                             "state-of-the-art crowd counting methods, especially when perspective " \
                                             "effects are strong. "
            elif b == 1 and (a == 1 and c == 0):
                submission.model_name_desc = "MSFANet: Encoder-Decoder Based Convolutional Neural Networks with" \
                                             " Multi-Scale-Aware Modules for Crowd Counting"
            else:
                submission.model_name_desc = "None of our models perform well on this image. We will expand your " \
                                             "options in the near future "
            if a and b and c:
                pred = "unsuccessful"
            else:
                pred = "successful"

            count = msfanet(submission.file)

        else:
            submission.message = "model is not connected yet"
            submission.status = Submission.FAILED
            submission.save()
    except Exception as e:
        submission.message = f"failed due to following error:\n {str(e)}"
        submission.status = Submission.FAILED
        submission.save()

        return

    submission.count = count
    submission.predict = pred
    submission.message = f"done at {datetime.now()}"
    submission.status = Submission.SUCCESS
    submission.save()
