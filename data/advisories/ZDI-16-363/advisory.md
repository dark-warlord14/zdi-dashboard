# ZDI-16-363: Hewlett Packard Enterprise LoadRunner Shared Memory Name Construction Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-363
- **ZDI-CAN:** ZDI-CAN-3516
- **Date:** 2016-06-03
- **CVE:** CVE-2016-4359
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** LoadRunner
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-363/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within mchan.dll when constructing a shared memory file name. The issue lies in the failure to validate the size of a user-supplied string prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-c05157423

## Disclosure Timeline

- 2016-01-26 - Vulnerability reported to vendor
- 2016-06-03 - Coordinated public release of advisory
