# ZDI-22-128: Oracle VirtualBox TFTP Server Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-128
- **ZDI-CAN:** ZDI-CAN-16026
- **Date:** 2022-01-21
- **CVE:** CVE-2022-21394
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-128/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the implementation of the TFTP server. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujan2022.html

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-01-21 - Coordinated public release of advisory
