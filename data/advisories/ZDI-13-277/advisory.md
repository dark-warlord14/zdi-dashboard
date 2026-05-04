# ZDI-13-277: Ecava IntegraXor Project Directory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-277
- **ZDI-CAN:** ZDI-CAN-1988
- **Date:** 2013-12-15
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Ecava
- **Affected Products:** IntegraXor
- **Credit:** Alphazorx aka technically.screwed
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-277/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Ecava IntegraXor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the storing of credentials in cleartext. The issue lies in the ability to bypass file access restrictions. This can be used along with the automatic creation of backup files, which are created whenever changes are made to a project. By abusing this flaw an attacker can disclose credentials and possibly leverage this situation to achieve remote code execution.

## Disclosure Timeline

- 2013-11-06 - Vulnerability reported to vendor
- 2013-12-15 - Coordinated public release of advisory
