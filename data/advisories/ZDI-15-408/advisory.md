# ZDI-15-408: Hewlett-Packard LoadRunner Controller Scenario File Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-408
- **ZDI-CAN:** ZDI-CAN-2756
- **Date:** 2015-09-01
- **CVE:** CVE-2015-5426
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LoadRunner
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-408/
## Vulnerability Details

This vulnerability could allow attackers to execute arbitrary code on vulnerable installations of HP LoadRunner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of scenario files (.lrs). By manipulating a scenario file's values, an attacker can cause a fixed-length stack buffer to overflow. An attacker could leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hpe.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04692147

## Disclosure Timeline

- 2015-03-31 - Vulnerability reported to vendor
- 2015-09-01 - Coordinated public release of advisory
