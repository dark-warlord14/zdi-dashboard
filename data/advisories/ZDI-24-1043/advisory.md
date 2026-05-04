# ZDI-24-1043: (0Day) (Pwn2Own) Pioneer DMH-WT7600NEX Media Service Improper Handling of Exceptional Conditions Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1043
- **ZDI-CAN:** ZDI-CAN-23302
- **Date:** 2024-08-01
- **CVE:** CVE-2024-23930
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Pioneer
- **Affected Products:** DMH-WT7600NEX
- **Credit:** NCC Group EDG (@nccgroupinfosec @_mccaulay @alexjplaskett)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1043/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of Pioneer DMH-WT7600NEX devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Media service, which listens on TCP port 42000 by default. The issue results from improper handling of error conditions. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

01/24/24 – ZDI reported the vulnerability to the vendor at Pwn2Own Automotive. 07/30/24 – ZDI asked for an update. 07/30/24 – The vendor states that they have been working on the vulnerability reported at Pwn2Own, but more countermeasures are required. They also stated that they would get back to us once they get a status update from their design department. 07/31/24 – ZDI informed the vendor that since the vulnerability remains unpatched, that we intend to publish the report as a zero-day advisory on 08/01/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application On 12/19/24 The vendor addressed the issue here: https://jpn.pioneer/ja/car/dl/dmh-sz700_sf700/

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-08-01 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
