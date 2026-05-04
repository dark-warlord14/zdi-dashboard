# ZDI-15-646: Mozilla Firefox HTMLVideoElement Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-646
- **ZDI-CAN:** ZDI-CAN-3176
- **Date:** 2015-12-18
- **CVE:** CVE-2015-4509
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-646/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of media objects. By manipulating a document's elements an attacker can cause a HTMLVideoElement object in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2015-106/

## Disclosure Timeline

- 2015-08-24 - Vulnerability reported to vendor
- 2015-12-18 - Coordinated public release of advisory
