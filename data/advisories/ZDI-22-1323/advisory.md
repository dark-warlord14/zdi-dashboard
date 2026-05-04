# ZDI-22-1323: (0Day) GE CIMPLICITY CIM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1323
- **ZDI-CAN:** ZDI-CAN-15575
- **Date:** 2022-09-29
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** GE
- **Affected Products:** CIMPLICITY
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1323/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GE CIMPLICITY. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CIM files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

03/02/22 – ZDI reported the vulnerability to ICS-CERT to coordinate with the vendor. 03/02/22 – The vendor acknowledged the vulnerability report. 05/20/22 – ICS-CERT asked for an update. 05/26/22 – The vendor stated that they are reviewing the case on 5/31/22. 05/31/22 – The vendor sent an update about the progress of the report. 07/19/22 – ICS-CERT asked for an update. 09/20/22 – ZDI informed the vendor that this case will be published as a zero-day advisory on 09/28/22. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-03-02 - Vulnerability reported to vendor
- 2022-09-29 - Coordinated public release of advisory
