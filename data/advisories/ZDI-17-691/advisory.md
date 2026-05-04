# ZDI-17-691: (0Day) Foxit Reader launchURL Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-691
- **ZDI-CAN:** ZDI-CAN-4724
- **Date:** 2017-08-17
- **CVE:** CVE-2017-10951
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-691/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within app.launchURL method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. "Foxit Reader & PhantomPDF has a Safe Reading Mode which is enabled by default to control the running of JavaScript, which can effectively guard against potential vulnerabilities from unauthorized JavaScript actions." 05/18/17 - ZDI disclosed report to vendor 06/22/17 - ZDI inquired about status 06/26/17 - Vendor indicated that they could not reproduce the issue 06/26/17 - ZDI provided repro steps 06/26/17 - Vendor requested further repro details 07/06/17 - ZDI replied with sample scenario and the re-iterated the need for a fix 07/20/17 - The vendor indicated this will not be fixed because this can be mitigated by Secure Mode 08/08/17 - ZDI communicated that the proposed mitigation is not a fix and that the case will move to 0-day status POST 0-day UPDATE: 08/26/17 - The vendor sent patch links to ZDI https://www.foxitsoftware.com/products/pdf-reader/ -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2017-05-18 - Vulnerability reported to vendor
- 2017-08-17 - Coordinated public release of advisory
