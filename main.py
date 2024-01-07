from src.red_wine_project.pipeline.Trainingpipeline import TrainPipeline


if __name__=='__main__':
    tr=TrainPipeline()
    if tr.is_running == False:
        tr.start_training()
        
    else:
        print("Pipeline is currently running")
