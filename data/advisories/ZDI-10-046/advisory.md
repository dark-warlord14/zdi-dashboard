# ZDI-10-046: Mozilla Firefox Web Worker Array Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-046
- **ZDI-CAN:** ZDI-CAN-624
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0160
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** Orlando Barrera II, SecTheory
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-046/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the implementation of web worker threads. Due to mishandling the array data type while processing posted messages, a web worker thread can be made to corrupt heap memory. An attacker can exploit this vulnerability to execute arbitrary code under the context of the user running the browser.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-02.html

## Disclosure Timeline

- 2009-12-04 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
