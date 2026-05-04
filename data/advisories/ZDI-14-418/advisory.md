# ZDI-14-418: BitTorrent Web Interface Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-418
- **ZDI-CAN:** ZDI-CAN-2352
- **Date:** 2014-12-09
- **CVE:** CVE-2014-8515
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** BitTorrent
- **Affected Products:** BitTorrent
- **Credit:** lokihardt@asrt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-418/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BitTorent. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the web interface bound to port 10000. By providing the right pairing values an attacker would be able to provide a command to be executed right after the torrent finishes the download. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

BitTorrent has issued an update to correct this vulnerability. More details can be found at: http://download-new.utorrent.com/endpoint/utorrent/os/windows/track/stable/

## Disclosure Timeline

- 2014-10-15 - Vulnerability reported to vendor
- 2014-12-09 - Coordinated public release of advisory
