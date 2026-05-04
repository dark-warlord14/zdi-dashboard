# ZDI-15-159: (Mobile Pwn2Own) Amazon App Store JavaScript Bridge Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-159
- **ZDI-CAN:** ZDI-CAN-2632
- **Date:** 2015-04-29
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Amazon
- **Affected Products:** App Store
- **Credit:** MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-159/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on Amazon Fire Phone. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the methods that were exposed to the WebView. The IntentBridge class wraps IPC functions that allows an attacker to download and install a malicious application. A remote attacker can abuse this achieve remote code execution under the context of the process.

## Additional Details

There was not an advisory posted and no patch required, the issue was fixed server side.

## Disclosure Timeline

- 2014-11-12 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
