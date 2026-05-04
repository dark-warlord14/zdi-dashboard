# ZDI-22-501: Microsoft Office Visio EMF EMR_COMMENT_EMFPLUS Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-501
- **ZDI-CAN:** ZDI-CAN-15764
- **Date:** 2022-03-09
- **CVE:** CVE-2022-24509
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-501/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of EMR_COMMENT_EMFPLUS records in EMF images. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-24509

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-03-09 - Coordinated public release of advisory
