# ZDI-25-083: Microsoft Edge ms-its: Scheme Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-083
- **ZDI-CAN:** ZDI-CAN-24690
- **Date:** 2025-02-04
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file while in Internet Explorer mode. The specific flaw exists within the handling of the ms-its: URI scheme. A crafted URI can result in unconstrained execution of script in a downloaded file, irrespective of the presence of the Mark-Of-The-Web. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2024-08-09 - Vulnerability reported to vendor
- 2025-02-04 - Coordinated public release of advisory
- 2025-02-04 - Advisory Updated
