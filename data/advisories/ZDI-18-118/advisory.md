# ZDI-18-118: Oracle VirtualBox crStatePixelMapuiv Stack-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-118
- **ZDI-CAN:** ZDI-CAN-5160
- **Date:** 2018-01-18
- **CVE:** CVE-2018-2686
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Vasily Vasiliev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-118/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crStatePixelMapuiv method. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujan2018-3236628.html

## Disclosure Timeline

- 2017-10-26 - Vulnerability reported to vendor
- 2018-01-18 - Coordinated public release of advisory
