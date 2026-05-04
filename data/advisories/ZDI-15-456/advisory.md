# ZDI-15-456: Mozilla Firefox MPEG4 saio Chunk Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-456
- **ZDI-CAN:** ZDI-CAN-2966
- **Date:** 2015-10-05
- **CVE:** CVE-2015-4479
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-456/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of MPEG4 media files. The issue lies in the failure to check for an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute arbitrary code within the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2015-83/

## Disclosure Timeline

- 2015-05-28 - Vulnerability reported to vendor
- 2015-10-05 - Coordinated public release of advisory
