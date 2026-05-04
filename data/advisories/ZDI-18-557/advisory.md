# ZDI-18-557: Samsung Email Arbitrary File Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-557
- **ZDI-CAN:** ZDI-CAN-5329
- **Date:** 2018-06-07
- **CVE:** CVE-2018-10498
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samsung
- **Affected Products:** Email
- **Credit:** Tencent Keen Security Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-557/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Samsung Email. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of file:/// URIs. The issue lies in the lack of proper validation of user-supplied data, which can allow for reading arbitrary files. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges.

## Additional Details

Market Update / 2018 Feb SMR O os: Patched with Samsung Email(5.0.02.16) in Store N os: Patched with Samsung Email(4.2.66.2) in Store M: Patched with 2018 FEB SMR

## Disclosure Timeline

- 2017-11-05 - Vulnerability reported to vendor
- 2018-06-07 - Coordinated public release of advisory
- 2018-06-07 - Advisory Updated
