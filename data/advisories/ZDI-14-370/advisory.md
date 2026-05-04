# ZDI-14-370: BitTorrent Bootstrap Improper Indexing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-370
- **ZDI-CAN:** ZDI-CAN-2494
- **Date:** 2014-10-29
- **CVE:** CVE-2014-8509
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** BitTorrent
- **Affected Products:** BitTorrent
- **Credit:** Daejin Lee
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-370/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BitTorrent Bootstrap. User interaction is not required to exploit this vulnerability. The specific flaw exists within the handling of arguments passed to the lazy_bdecode function. By sending a specific crafted packet an attacker can access data outside the bounds of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

BitTorrent has issued an update to correct this vulnerability. More details can be found at: https://github.com/bittorrent/bootstrap-dht/commit/bbc0b7191e3f48461ca6e5b1b34bdf4b3f1e79a9

## Disclosure Timeline

- 2014-10-15 - Vulnerability reported to vendor
- 2014-10-29 - Coordinated public release of advisory
