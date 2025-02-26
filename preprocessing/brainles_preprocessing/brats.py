from brainles_preprocessing.core import modality_centric_atlas_preprocessing, Modality


def brats_style_t1c_centric_preprocessing(
    input_t1c: str,
    output_t1c: str,
    input_t1: str,
    output_t1: str,
    input_t2: str,
    output_t2: str,
    input_flair: str,
    output_flair: str,
    bet_mode: str = "gpu",
    limit_cuda_visible_devices: str = None,
    keep_coregistration: str = None,
    keep_atlas_registration: str = None,
    keep_brainextraction: str = None,
):
    primary = Modality(
        modality_name="t1c",
        input_path=input_t1c,
        output_path=output_t1c,
        bet=True,
    )

    moving_modalities = [
        Modality(
            modality_name="t1",
            input_path=input_t1,
            output_path=output_t1,
            bet=True,
        ),
        Modality(
            modality_name="t2",
            input_path=input_t2,
            output_path=output_t2,
            bet=True,
        ),
        Modality(
            modality_name="flair",
            input_path=input_flair,
            output_path=output_flair,
            bet=True,
        ),
    ]

    modality_centric_atlas_preprocessing(
        primary_modality=primary,
        moving_modalities=moving_modalities,
        bet_mode=bet_mode,
        limit_cuda_visible_devices=limit_cuda_visible_devices,
        keep_coregistration=keep_coregistration,
        keep_atlas_registration=keep_atlas_registration,
        keep_brainextraction=keep_brainextraction,
    )


def brats_style_t1_centric_preprocessing(
    input_t1: str,
    output_t1: str,
    input_t1c: str,
    output_t1c: str,
    input_t2: str,
    output_t2: str,
    input_flair: str,
    output_flair: str,
    bet_mode: str = "gpu",
    limit_cuda_visible_devices: str = None,
    keep_coregistration: str = None,
    keep_atlas_registration: str = None,
    keep_brainextraction: str = None,
):
    primary = Modality(
        modality_name="t1",
        input_path=input_t1,
        output_path=output_t1,
        bet=True,
    )

    moving_modalities = [
        Modality(
            modality_name="t1c",
            input_path=input_t1c,
            output_path=output_t1c,
            bet=True,
        ),
        Modality(
            modality_name="t2",
            input_path=input_t2,
            output_path=output_t2,
            bet=True,
        ),
        Modality(
            modality_name="flair",
            input_path=input_flair,
            output_path=output_flair,
            bet=True,
        ),
    ]

    modality_centric_atlas_preprocessing(
        primary_modality=primary,
        moving_modalities=moving_modalities,
        bet_mode=bet_mode,
        limit_cuda_visible_devices=limit_cuda_visible_devices,
        keep_coregistration=keep_coregistration,
        keep_atlas_registration=keep_atlas_registration,
        keep_brainextraction=keep_brainextraction,
    )
