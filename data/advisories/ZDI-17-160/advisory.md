# ZDI-17-160: Hewlett Packard Enterprise LoadRunner libxdrutil mxdr_string Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-160
- **ZDI-CAN:** ZDI-CAN-3933
- **Date:** 2017-03-09
- **CVE:** CVE-2017-5789
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** LoadRunner
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-160/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within the libxdrutil.dll mxdr_string method. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20565.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-hpesbgn03712en_us

## Disclosure Timeline

- 2016-11-30 - Vulnerability reported to vendor
- 2017-03-09 - Coordinated public release of advisory
