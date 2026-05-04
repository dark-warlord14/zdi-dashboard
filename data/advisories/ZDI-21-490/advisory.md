# ZDI-21-490: (0Day) Advantech WebAccess/HMI Designer PM3 File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-490
- **ZDI-CAN:** ZDI-CAN-12276
- **Date:** 2021-04-28
- **CVE:** CVE-2021-33000
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/HMI Designer
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-490/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess/HMI Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PM3 files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 11/24/20 - ZDI reported the vulnerabilities to ICS-CERT 03/31/21 - ZDI requested an update 04/02/20 - ICS-CERT confirmed receipt of the reports 04/06/21 - ZDI requested an update 04/13/21 - ICS-CERT communicated that the cases had been fixed 04/08/21 - ZDI requested an advisory 04/08/21 - ICS-CERT confirmed that an advisory draft would be provided by the following week 04/14/21 - ICS-CERT requested technical clarification 04/15/21 - ZDI provided additional evidence 04/20/21 - ZDI notified ICS-CERT of the intention to publish this report as a 0-day advisories on 04/28/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-12-02 - Vulnerability reported to vendor
- 2021-04-28 - Coordinated public release of advisory
