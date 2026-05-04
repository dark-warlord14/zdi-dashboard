# ZDI-23-837: NETGEAR RAX30 USB Share Link Following Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-837
- **ZDI-CAN:** ZDI-CAN-19498
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34283
- **CVSS:** 4.6
- **CVSS Vector:** AV:P/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-837/
## Vulnerability Details

This vulnerability allows physically present attackers to disclose sensitive information on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of symbolic links on removable USB media. By creating a symbolic link, an attacker can abuse the router's web server to access arbitrary local files. An attacker can leverage this vulnerability to disclose information in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065650/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2023-0003-PSV-2023-0004?article=000065650

## Disclosure Timeline

- 2023-01-04 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
