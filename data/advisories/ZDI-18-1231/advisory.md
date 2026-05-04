# ZDI-18-1231: Oracle VirtualBox crServerDispatchGetAttachedObjectsARB Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1231
- **ZDI-CAN:** ZDI-CAN-6634
- **Date:** 2018-10-15
- **CVE:** CVE-2018-3086
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Root Object
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1231/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crServerDispatchGetAttachedObjectsARB method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpujul2018-4258247.html

## Disclosure Timeline

- 2018-07-10 - Vulnerability reported to vendor
- 2018-10-15 - Coordinated public release of advisory
- 2018-10-15 - Advisory Updated
