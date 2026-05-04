# ZDI-15-455: VMware vCenter Server JMX RMI Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-455
- **ZDI-CAN:** ZDI-CAN-2763
- **Date:** 2015-10-02
- **CVE:** CVE-2015-2342
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** VMware, Inc.
- **Affected Products:** VMware Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-455/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of VMware vCenter Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the configuration of the JMX remote interface. This interface allows a remote attacker to register attacker-controlled mbeans. This vulnerability can be leveraged by an attacker to gain remote code execution under the context of SYSTEM.

## Additional Details

VMware, Inc. has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2015-0007

## Disclosure Timeline

- 2015-04-07 - Vulnerability reported to vendor
- 2015-10-02 - Coordinated public release of advisory
