<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Summary</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

<body>
<h1>Bistability analysis of excitatory, inhibitory and somatostatin neuron network</h1>

<!-- Table of Contents -->
<h2>Table of Contents</h2>
<ul>
  <li><a href="#Introduction">Introduction</a></li>
  <li><a href="#Integrate-and-fire-model">Integrate and fire model</a></li>
  <li><a href="#Quadratic-Integrate-and-fire-model">Quadratic Integrate and fire model model</a></li>
  <li><a href="#Theta-model">Theta model</a></li>
</ul>


<!-- Sections -->
<!-- Introduction Section -->
<h2 id="Introduction">Introduction</h2>
<p>Recently we have seen a lot of studies of E + I neuron networks, spiking models,
   γ oscillatory neurons, etc. Recent studies indicate the importance of the other populations 
   of inhibitory interneurons. The E + I network is specifically Pyramidal cells (E) and Parvalbumin(I) cells,
    notably, somatostatin neurons(I). They have different temporal properties and different connectivities. 
    The goal of this paper is to explore the dynamics when there are 3 populations of cells.
</p>




<!-- IF Section -->
<h2 id="Integrate-and-fire-model">Integrate and fire model</h2>
<p>The Integrate-and-Fire neuron is a simplified computational model that simulates the membrane potential 
  of a neuron, integrating incoming electrical signals until a threshold is reached, at which point it "fires" 
  (generates an action potential) and then resets its membrane potential. This model captures the basic behavior
   of neuronal spiking in response to synaptic inputs.
   The right hand side RC circuit model 
  $$\tau \frac{dy}{dx}=-(u-u_{rest})+RI$$
<p>
  <p><img src="images/IF.png" alt="Integrate-and-fire-model w.r.t current inputs"></p>




  <!-- QIF Section -->
<h2 id="Quadratic-Integrate-and-fire-model">Quadratic Integrate and fire model</h2>
<p>In an EF model  
                        $$\tau \frac{𝑑𝑢}{𝑑𝑡}=𝐹(𝑢)$$
If we have $F(u)$ a quadratic equation then the model will be called Quadratic Integrate and fire neuron; QIF. 

In the RHS video I have used 
 $$𝐹(𝑢)=𝑢^2−𝑎^2+𝐼. $$
The input current is 30 and 50 at time 50 and 300.

<p><video controls>
        <source src="videos/qif_neuron_simulation.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video></p>




  <!-- Theta Section -->
<h2 id="Theta-model">Theta model</h2>
<p>If we put $𝑢=\tan⁡\frac{𝜃}{2}$ then our equation $$\tau \frac{𝑑𝑢}{𝑑𝑡}=𝑢^2−𝑎^2+𝐼$$ will become
$$\tau \frac{𝑑\theta}{𝑑𝑡}=(1−\sin⁡\theta)−𝑎^2 (\cos⁡\theta+1)+𝐼(\cos⁡\theta+1)$$
This is a Theta model.</p>





  <!-- Network Section -->
<h2 id="Network">Mathematical Analysis</h2>
<p><img src="images/Network.png" alt="Our studied network"></p>


<h2 id="Mathematical-Analysis">Mathematical Analysis</h2>
<h3>How do we relate population to spiking model</h3>
<p>
So the first step is to consider a large population of $N$ globally coupled quadratic integrate and fire neurons (QIF):
$$
\tau_m \frac{d V_j}{d t}=V_j^2+\mu(t)+\Delta \xi_j+g S
$$
where $\mu(t)$ is global (to every neuron) drive, $\Delta$ is a heterogeneity strength, $\xi_j$ is taken from some symmetric distribution centered at $0, q(\xi)$, but fixed in time, and $S$ satisfies:
$$
\tau_s \frac{d S}{d t}=-S+\frac{1}{N} \sum_{j=1}^N \sum_k \delta\left(t-t_j^k\right)\tau_m .
$$
    
The times $t_j^k$ satisfy

$$
\lim _{t \rightarrow t_j^k} V_j(t)=+\infty
$$
and are the times that neuron $j$ fires a spike and $V_j$ is set to $-\infty$. So every neuron is connected to every other one through the synaptic drive, gS. Let $P(V, \xi, t)$ denote the probability density for the voltages. That is $P(V, \xi, t)$ is the probability of a randomly chosen neuron having a voltage $v$ and hetereogeneity, $\xi$ at time $t$. Let \(f(V, \xi, t)=V^2+\mu(t)+\Delta \xi+g S\). Then, the probability density evolves as:
\begin{equation}
    \tau_m \frac{\partial P(V, \xi, t)}{\partial t}+\frac{\partial}{\partial V}(f(V, \xi, t) P(V, \xi, t))=0
\end{equation}

The flux $J(V, \xi, t) =\frac{f(V, \xi, t) P(V, \xi, t)}{\tau_m}$ is the rate at which a neuron crosses $V$. The firing rate of a neuron with parameter $\xi$ at time $t$ is
$$
R(\xi, t)=\lim _{V \rightarrow \infty} J(V, \xi, t)
$$
and the mean firing rate is
$$
r(t)=\int_{-\infty}^{\infty} q(\xi) R(\xi, t) d \xi .
$$
where $$q(\xi)=\frac{1}{\pi}\frac{1}{1+\xi^2}$$
</p>




   
    

