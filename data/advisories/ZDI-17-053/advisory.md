# ZDI-17-053: Samba NDR Parsing ndr_pull_dnsp_name Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-053
- **ZDI-CAN:** ZDI-CAN-3995
- **Date:** 2017-01-20
- **CVE:** CVE-2016-2123
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Samba
- **Affected Products:** 4.x
- **Credit:** c4c1234757b4f1e468a29d480d78f21b Frederic Besler c692f9f0933f03c265e4c9e2bcc3bb28
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Samba. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of NDR data. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of current process.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: https://www.samba.org/samba/security/CVE-2016-2123.html

## Disclosure Timeline

- 2016-11-04 - Vulnerability reported to vendor
- 2017-01-20 - Coordinated public release of advisory
