# step 1 & 2

_# STEP 1
## Flask Hello World 
This is a simple P Flask application that returns "Hello, World!" when accessed.
## How to Run with Docker
## 1. Build the Docker image
docker-compose build
## 2.Check the app work online 
docker-compose up  
## 3.Check the images name because docker generate automaticly if not given
docker images    
## 4.Tag and push the image to docker HUB
docker tag project-flask-app thepankrat/flask-hello
docker push thepankrat/flask-hello 

# STEP 2
## 1.run the image in the background and checking local host : http://localhost:5000/
docker run -d -p 5000:5000 flask-hello

## volumes manggment for my simple app not needed but if needed need to add in docker compose 
volumes:
      - ./my_host_folder:/my_container_folder_

---

## 🚀 Phase 4: Advanced Automation – GitOps & Monitoring

This phase implements a complete GitOps workflow using ArgoCD and sets up monitoring with Prometheus and Grafana.

### 1. GitOps with ArgoCD

This project uses ArgoCD to automatically sync the cluster's state with the code in this Git repository.

* **ArgoCD UI:** Can be accessed by port-forwarding:
    ```bash
    kubectl port-forward svc/argocd-server -n argocd 8080:443
    ```
    Then open `https://localhost:8080`.

* **Application Manifests:** The ArgoCD application definitions are stored in the `/argocd-apps` folder.
    * `quake-watch-app.yaml`: Deploys our Flask application from the `/my-app-chart` Helm chart.
    * `monitoring-app.yaml`: Deploys the `kube-prometheus-stack` to the `monitoring` namespace.

Any changes pushed to the `develop` branch (like updating the Helm chart) will be detected by ArgoCD and automatically synced to the cluster.

### 2. Monitoring with Prometheus & Grafana

The monitoring stack is also managed by ArgoCD.

* **Grafana UI:** Can be accessed by port-forwarding:
    ```bash
    kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80
    ```
    Then open `http://localhost:3000`. The username is `admin` and the password can be retrieved with:
    ```bash
    kubectl get secret monitoring-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 -d
    ```

* **Dashboards:** The stack includes many pre-built dashboards. The most useful one for our app is:
    * **Dashboard:** `Kubernetes / Compute Resources / Namespace (Pods)`
    * **Filter:** Select the `quake-watch-prod` namespace.

* **Alerting:** We have one active alert:
    * **Name:** `QuakeWatch High CPU`
    * **Condition:** Fires if the average CPU for the `quake-watch-prod` namespace goes above 10% (0.1) for 1 minute.