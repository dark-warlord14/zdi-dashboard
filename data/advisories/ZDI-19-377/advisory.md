# ZDI-19-377: Oracle VirtualBox CRClientPointer Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-377
- **ZDI-CAN:** ZDI-CAN-7363
- **Date:** 2019-04-17
- **CVE:** CVE-2019-2657
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Jason Matthyser (pleasew8t) of MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-377/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the handling of the CRClientPointer pointer. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuapr2019-5072813.html

## Disclosure Timeline

- 2018-10-14 - Vulnerability reported to vendor
- 2019-04-17 - Coordinated public release of advisory
