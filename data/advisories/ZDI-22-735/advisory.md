# ZDI-22-735: Microsoft Windows Print Spooler Service Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-735
- **ZDI-CAN:** ZDI-CAN-16215
- **Date:** 2022-05-10
- **CVE:** CVE-2022-29140
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Oliver Lyak (@ly4k_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-735/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Print Spooler service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to disclose information in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-29140

## Disclosure Timeline

- 2022-02-23 - Vulnerability reported to vendor
- 2022-05-10 - Coordinated public release of advisory
