# ZDI-21-1031: (0Day) Fuji Electric Tellus Lite V-Simulator 6 V9 File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1031
- **ZDI-CAN:** ZDI-CAN-13292
- **Date:** 2021-08-30
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Tellus Lite
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Tellus Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of V9 files in the V-Simulator 6 module. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/12/21 – ZDI reported the vulnerabilities to ICS-CERT 03/12/21 – ICS-CERT acknowledged the reports 08/19/21 – ZDI requested an update 08/19/21 – ICS-CERT indicated the fix was scheduled for October 08/19/21 – ZDI notified ICS-CERT of the intention to publish the cases as 0-day advisories on 08/30/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-03-12 - Vulnerability reported to vendor
- 2021-08-30 - Coordinated public release of advisory
