# ZDI-18-1059: (0Day) Wecon PLC Editor prg_ldview DevCmt Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1059
- **ZDI-CAN:** ZDI-CAN-6252
- **Date:** 2018-09-17
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Wecon
- **Affected Products:** PLC Editor
- **Credit:** Natnael Samson(Natti)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1059/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon PLC Editor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WCP files. When parsing the DevCmt element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/18/18 - ZDI reported the vulnerability to ICS-CERT 05/30/18 - ICS-CERT acknowledged receipt of the report, indicated this was provided to the vendor and provided an ICS-VU # 08/20/18 - ICS-CERT indicated that the vendor acknowledged the report but had not replied since that time 09/12/18 - ZDI notified ICS-CERT of the intention to disclose the report as 0-day on 9/17/18 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-05-18 - Vulnerability reported to vendor
- 2018-09-17 - Coordinated public release of advisory
- 2018-09-17 - Advisory Updated
