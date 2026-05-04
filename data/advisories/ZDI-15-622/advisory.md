# ZDI-15-622: Foxit PhantomPDF Print Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-622
- **ZDI-CAN:** ZDI-CAN-3075
- **Date:** 2015-12-08
- **CVE:** CVE-2015-8580
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-622/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Print method. A specially crafted PDF document can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php#FRD-36

## Disclosure Timeline

- 2015-07-28 - Vulnerability reported to vendor
- 2015-12-08 - Coordinated public release of advisory
