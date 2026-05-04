# ZDI-15-158: (Mobile Pwn2Own) Amazon App Store Search String Cross-Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-158
- **ZDI-CAN:** ZDI-CAN-2617
- **Date:** 2015-04-29
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Amazon
- **Affected Products:** App Store
- **Credit:** MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-158/
## Vulnerability Details

This vulnerability allows remote attackers to inject scripts on Amazon Fire Phone. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the search string variable. Starting the string with a closing script tag allows the attacker to insert HTML code. An attacker can chain this vulnerability with other vulnerabilities to install malicious applications.

## Additional Details

There was not an advisory posted and no patch required, the issue was fixed server side.

## Disclosure Timeline

- 2014-11-13 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
