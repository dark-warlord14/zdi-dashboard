# ZDI-24-1044: (0Day) (Pwn2Own) Pioneer DMH-WT7600NEX Telematics Directory Traversal Arbitrary File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1044
- **ZDI-CAN:** ZDI-CAN-23301
- **Date:** 2024-08-01
- **CVE:** CVE-2024-23929
- **CVSS:** 7.3
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H
- **Affected Vendors:** Pioneer
- **Affected Products:** DMH-WT7600NEX
- **Credit:** NCC Group EDG (@nccgroupinfosec @_mccaulay @alexjplaskett)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1044/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create arbitrary files on affected installations of Pioneer DMH-WT7600NEX devices. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the telematics functionality. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

01/24/24 – ZDI reported the vulnerability to the vendor at Pwn2Own Automotive. 07/30/24 – ZDI asked for an update. 07/30/24 – The vendor states that they have been working on the vulnerability reported at Pwn2Own, but more countermeasures are required. They also stated that they would get back to us once they get a status update from their design department. 07/31/24 – ZDI informed the vendor that since the vulnerability remains unpatched, that we intend to publish the report as a zero-day advisory on 08/01/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application On 12/19/24 The vendor addressed the issue here: https://jpn.pioneer/ja/car/dl/dmh-sz700_sf700/

## Disclosure Timeline

- 2024-02-02 - Vulnerability reported to vendor
- 2024-08-01 - Coordinated public release of advisory
- 2025-03-25 - Advisory Updated
