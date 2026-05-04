# ZDI-16-364: Hewlett Packard Enterprise LoadRunner Virtual Table Server import_csv Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-364
- **ZDI-CAN:** ZDI-CAN-3555
- **Date:** 2016-06-03
- **CVE:** CVE-2016-4360
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:P/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** LoadRunner
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-364/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Hewlett Packard Enterprise LoadRunner. Authentication is not required to exploit this vulnerability. The specific flaw exists within the import_csv functionality. The issue lies in the failure to restrict file paths sent to an unlink call which allows for the deletion of arbitrary files as SYSTEM. A remote attacker can leverage this vulnerability to cause a denial-of-service condition.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hpe.com/hpsc/doc/public/display?docId=emr_na-c05157423

## Disclosure Timeline

- 2016-02-12 - Vulnerability reported to vendor
- 2016-06-03 - Coordinated public release of advisory
