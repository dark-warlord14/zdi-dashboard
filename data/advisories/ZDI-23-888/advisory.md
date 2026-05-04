# ZDI-23-888: Adobe Substance 3D Designer SBS File Parsing Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-888
- **ZDI-CAN:** ZDI-CAN-20963
- **Date:** 2023-06-16
- **CVE:** CVE-2023-21618
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Substance 3D Designer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-888/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Substance 3D Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SBS files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/substance3d_designer/apsb23-39.html

## Disclosure Timeline

- 2023-04-26 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
