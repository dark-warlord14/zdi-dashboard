# ZDI-06-009: Mozilla Firefox Tag Parsing Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-009
- **ZDI-CAN:** ZDI-CAN-008
- **Date:** 2006-04-17
- **CVE:** CVE-2006-0749
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 1.0.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-009/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of the Mozilla/Firefox web browser and Thunderbird e-mail client. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious e-mail. The specific flaw exists within nsHTMLContentSink.cpp, during the parsing of HTML tags as they appear in a specific order. The flaw results in a memory corruption that leads to an attacker controlled function pointer dereference from the stack and eventually execution of arbitrary code.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2006/mfsa2006-18.html

## Disclosure Timeline

- 2005-12-13 - Vulnerability reported to vendor
- 2006-04-17 - Coordinated public release of advisory
