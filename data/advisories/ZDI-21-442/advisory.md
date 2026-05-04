# ZDI-21-442: (0Day) Advantech WebAccess/HMI Designer SNF File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-442
- **ZDI-CAN:** ZDI-CAN-12477
- **Date:** 2021-06-24
- **CVE:** CVE-2021-33004
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/HMI Designer
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-442/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess/HMI Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SNF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 12/02/20 – ZDI reported the vulnerability to ICS-CERT 04/02/21 – ICS-CERT indicated the vendor was working on a fix 04/06/21 – ZDI requested an update 04/06/21 – ICS-CERT indicated the vendor was working on a fix 04/08/21 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 04/20/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-06-24 - Coordinated public release of advisory
