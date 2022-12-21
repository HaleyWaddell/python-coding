Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
class LinearTopo(Topo):
  "Linear topology of k switches, with one host per switch."
  def __init__(self, k=2, **opts):
      """Init.
          k: number of switches (and hosts)
          hconf: host configuration options
          lconf: link configuration options"""
      super(LinearTopo, self).__init__(**opts)
      self.k = k
      lastSwitch = None
      for i in irange(1, k):
          host = self.addHost('h%s' % i, cpu=.5/k)
          switch = self.addSwitch('s%s' % i)
          # 10 Mbps, 5ms delay, 1% loss, 1000 packet queue
          self.addLink( host, switch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
          if lastSwitch:
              self.addLink(switch, lastSwitch, bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
          lastSwitch = switch
