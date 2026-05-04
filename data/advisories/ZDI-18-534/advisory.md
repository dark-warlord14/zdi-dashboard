# ZDI-18-534: (0Day) Microsoft Windows JScript Error Object Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-534
- **ZDI-CAN:** ZDI-CAN-5613
- **Date:** 2018-05-29
- **CVE:** CVE-2018-8267
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Dmitri Kaslov Telspace Systems
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-534/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Error objects in JScript. By performing actions in script, an attacker can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 01/23/18 - ZDI sent the vulnerability report to the vendor 01/23/18 - The vendor acknowledged and provided a case number 04/23/18 - The vendor replied that they were having difficulty reproducing the issue report without POC 04/24/18 - ZDI confirmed the POC was sent with the original and sent it again 05/01/18 - The vendor acknowledged receipt of the POC 05/08/18 - The vendor requested an extension 05/18/18 - ZDI replied "We have verified that we sent the POC with the original. The report will 0-day on May 29." -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2018-01-23 - Vulnerability reported to vendor
- 2018-05-29 - Coordinated public release of advisory
- 2018-06-04 - Advisory Updated
