# ZDI-22-1164: (0Day) Tencent WeChat WXAM Decoder Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1164
- **ZDI-CAN:** ZDI-CAN-16212
- **Date:** 2022-08-23
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1164/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WXAM decoder. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120-day timeline. 12/30/21 – ZDI reported the vulnerability to the vendor. 12/30/21 – The vendor acknowledged the vulnerability report. 05/17/22 – ZDI notified the vendor of the intention to publish the case as a zero-day advisory on May 31st, 2022. 05/19/22 – The vendor advised that the vulnerabilities were fixed in WeChat Android Version 8.0 22 was released on April 29th. 05/26/22 – ZDI advised the vendor that this vulnerability can still be reproduced in the latest release. 05/26/22 – The vendor requested additional technical details, which ZDI provided. 05/27/22 – The vendor states that they cannot reproduce the vulnerability in the latest release. 05/30/22 – ZDI provided additional technical details. 06/07/22 – The vendor states that they cannot reproduce the vulnerability in the latest release. 06/29/22 – ZDI provided additional technical details. 08/03/22 – ZDI notified the vendor of the intention to publish the case as a zero-day advisory on August 23rd, 2022. 08/10/22 – The vendor states that they cannot reproduce the vulnerability in the latest release. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
