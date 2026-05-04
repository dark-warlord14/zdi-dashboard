# ZDI-24-378: Ivanti Avalanche WLAvalancheService Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-378
- **ZDI-CAN:** ZDI-CAN-22827
- **Date:** 2024-04-23
- **CVE:** CVE-2024-23532
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-378/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ivanti Avalanche. Authentication is required to exploit this vulnerability. The specific flaw exists within the WLAvalancheService, which listens on TCP port 1777 by default. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated array. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-6-4-3-Security-Hardening-and-CVEs-addressed?language=en_US

## Disclosure Timeline

- 2023-12-13 - Vulnerability reported to vendor
- 2024-04-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
