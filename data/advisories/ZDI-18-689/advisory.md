# ZDI-18-689: Oracle VirtualBox crUnpackTexImage2D Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-689
- **ZDI-CAN:** ZDI-CAN-6234
- **Date:** 2018-07-18
- **CVE:** CVE-2018-3089
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-689/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crUnpackTexImage2D method. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujul2018-4258247.html

## Disclosure Timeline

- 2018-05-29 - Vulnerability reported to vendor
- 2018-07-18 - Coordinated public release of advisory
- 2018-07-18 - Advisory Updated
