# ZDI-18-688: Oracle VirtualBox crUnpackPixelMapuiv Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-688
- **ZDI-CAN:** ZDI-CAN-6236
- **Date:** 2018-07-18
- **CVE:** CVE-2018-3088
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-688/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the crUnpackPixelMapuiv method. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/security-advisory/cpujul2018-4258247.html

## Disclosure Timeline

- 2018-05-29 - Vulnerability reported to vendor
- 2018-07-18 - Coordinated public release of advisory
- 2018-07-18 - Advisory Updated
