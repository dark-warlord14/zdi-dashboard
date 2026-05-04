# ZDI-19-1035: Tencent WeChat name Field Unsafe Redirection Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1035
- **ZDI-CAN:** ZDI-CAN-9302
- **Date:** 2019-12-31
- **CVE:** CVE-2019-17151
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Todd Han and Junzhi Lu of TrendMicro Mobile Security Research Team, Zhengyu Dong
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1035/
## Vulnerability Details

This vulnerability allows remote attackers redirect users to an external resource on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must be within a chat session together with the attacker. The specific flaw exists within the parsing of a users profile. The issue lies in the failure to properly validate a users name. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

This issue has already been fixed in the latest online version, 7.0.9.

## Disclosure Timeline

- 2019-08-13 - Vulnerability reported to vendor
- 2019-12-31 - Coordinated public release of advisory
- 2020-01-08 - Advisory Updated
