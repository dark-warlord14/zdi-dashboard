# ZDI-19-145: (0Day) Wecon LeviStudioU DataLogTool Edit Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-145
- **ZDI-CAN:** ZDI-CAN-6347
- **Date:** 2019-01-29
- **CVE:** CVE-2019-6537
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Wecon
- **Affected Products:** LeviStudioU
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-145/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within DataLogTool.exe. During the Edit procedure, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/08/18 - ZDI provided 3 reports to the ICS-CERT 06/13/18 - ICS-CERT provided an ICS-VU# 09/25/18 - ZDI requested a status 09/26/18 - ICS-CERT advised that they requested status from the vendor on 09/18/18 and were awaiting a reply 11/15/18 - ICS-CERT advised only that the vendor was "currently working the issues reported" 11/26/18 - ZDI requested an ETA from ICS-CERT who indicated they requested this 12/06/18 - ICS-CERT advised ZDI that the vendor was "in the process of testing their update" and indicated "possibility of release in 2 weeks" 01/09/19 - ZDI advised ICS-CERT of the intention to 0-day publish 01/25/19 - ZDI telephoned ICS-CERT to discuss status and 0-day publish -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-06-08 - Vulnerability reported to vendor
- 2019-01-29 - Coordinated public release of advisory
- 2019-02-12 - Advisory Updated
