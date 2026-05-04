# ZDI-13-209: Hewlett-Packard LoadRunner lrLRIServices ActiveX Control SetOutputDirectory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-209
- **ZDI-CAN:** ZDI-CAN-1736
- **Date:** 2013-08-13
- **CVE:** CVE-2013-4801
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-209/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LoadRunner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the lrLRIServices ActiveX control. The issue lies in the handling of input to the output directory mutator. By calling this function twice, an attacker can ensure this memory is under control and leverage this situation to achieve remote code execution under the context of the current process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03862772

## Disclosure Timeline

- 2013-01-22 - Vulnerability reported to vendor
- 2013-08-13 - Coordinated public release of advisory
