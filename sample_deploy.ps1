# Set variables
$PROJECT_ID = "your-gcp-project-id"
$REGION = "us-central1"
$SERVICE_NAME = "laptop-price-api"
$IMAGE_NAME = "gcr.io/$PROJECT_ID/$SERVICE_NAME"

Write-Host "🔧 Building Docker image and deploying to Cloud Run..."

# Submit the build to Cloud Build and push image to Container Registry
gcloud builds submit --tag $IMAGE_NAME

# Deploy to Cloud Run
gcloud run deploy $SERVICE_NAME `
  --image $IMAGE_NAME `
  --platform managed `
  --region $REGION `
  --allow-unauthenticated `
  --port 8080

Write-Host "✅ Deployment complete!"
