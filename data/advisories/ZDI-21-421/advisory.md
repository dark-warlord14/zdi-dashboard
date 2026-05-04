# ZDI-21-421: Microsoft Windows Raw Image Extension CR3 File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-421
- **ZDI-CAN:** ZDI-CAN-12472
- **Date:** 2021-04-19
- **CVE:** CVE-2021-28468
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Raw Image Extension
- **Credit:** Wenguang Jiao
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-421/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Raw Image Extension. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CR3 images. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current user at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-28468

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-04-19 - Coordinated public release of advisory
