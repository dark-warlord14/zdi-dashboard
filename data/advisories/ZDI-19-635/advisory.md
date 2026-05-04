# ZDI-19-635: Foxit Reader Format String Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-635
- **ZDI-CAN:** ZDI-CAN-8544
- **Date:** 2019-07-05
- **CVE:** CVE-2019-13318
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** banananapenguin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-635/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the util.printf Javascript method. The application processes the %p parameter in the format string, allowing heap addresses to be returned to the script. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2019-06-13 - Vulnerability reported to vendor
- 2019-07-05 - Coordinated public release of advisory
