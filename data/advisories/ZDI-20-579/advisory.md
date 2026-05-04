# ZDI-20-579: Adobe After Effects MP4 File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-579
- **ZDI-CAN:** ZDI-CAN-10090
- **Date:** 2020-04-30
- **CVE:** CVE-2020-3765
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** After Effects
- **Credit:** Mat Powell & Michael DePlante of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-579/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe After Effects. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of MP4 files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/in/security/products/after_effects/apsb20-09.html

## Disclosure Timeline

- 2020-01-07 - Vulnerability reported to vendor
- 2020-04-30 - Coordinated public release of advisory
- 2020-07-20 - Advisory Updated
