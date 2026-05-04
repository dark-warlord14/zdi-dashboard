# ZDI-19-013: (0Day) Microsoft Windows vcf File Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-013
- **ZDI-CAN:** ZDI-CAN-6920
- **Date:** 2019-01-10
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** John Page (aka hyp3rlinx)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-013/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of VCard files. Crafted data in a VCard file can cause Windows to display a dangerous hyperlink. The user interface fails to provide any indication of the hazard. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

08/06/18 - ZDI reported the vulnerability to the vendor 08/07/18 - The vendor acknowledged the report and provided a tracking # 10/01/18 – The vendor requested an additional file 10/03/18 – ZDI provided added files and a new PoC 10/03/18 – The vendor advised the report did not meet the bar for service 10/05/18 – ZDI advised that we believe the report is exploitable and notified the vendor of the intent to 0-day on 10/16/18 10/08/18 – The vendor advised ZDI they had re-considered a fix and requested an extension to 01/08/19 10/09/18 – ZDI agreed to the short extension 11/14/18 – The vendor again advised ZDI of the target patch date 01/08/19 12/12/18 – The vendor provided ZDI a CVE 12/19/18 - The vendor wrote to ZDI to advise that “engineering team had decided to pursue the fix as v.Next” and “Microsoft has decided that it will not be fixing this vulnerability and we are closing this case” 12/27/18 – ZDI notified the vendor of the intent to 0-day on 01/07/18

## Disclosure Timeline

- 2018-09-06 - Vulnerability reported to vendor
- 2019-01-10 - Coordinated public release of advisory
- 2019-05-30 - Advisory Updated
