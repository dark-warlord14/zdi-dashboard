# ZDI-15-236: Google Chrome SpeechRecognitionClient Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-236
- **ZDI-CAN:** ZDI-CAN-2707
- **Date:** 2015-05-19
- **CVE:** CVE-2015-1251
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-236/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within SpeechRecognitionClient. By manipulating a document's elements, an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2015/05/stable-channel-update_19.html

## Disclosure Timeline

- 2015-02-05 - Vulnerability reported to vendor
- 2015-05-19 - Coordinated public release of advisory
